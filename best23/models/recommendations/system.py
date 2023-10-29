import json
import numpy as np
from sklearn.metrics.pairwise import cosine_distances
from sklearn.neighbors import KNeighborsClassifier
from best23.prepare_data import process_data, EMBEDDER

def load(path: str) -> dict:
    with open(path, "r") as file:
        return json.load(file)


class Recommender:
    def __init__(self) -> None:
        self.setup()

    def refresh(self) -> None:
        self.setup()
    
    def setup(self):
        # process_data("/home/mb-pro-kg/best23/data/culture.json")
        # process_data("/home/mb-pro-kg/best23/data/sightseeing.json")
        # process_data("/home/mb-pro-kg/best23/data/recreation.json")
        process_data("/home/mb-pro-kg/best23/data/users.json")

        culture = load("/home/mb-pro-kg/best23/data/culture_processed.json")
        sightseeing = load("/home/mb-pro-kg/best23/data/sightseeing_processed.json")
        recreation = load("/home/mb-pro-kg/best23/data/recreation_processed.json")
        users = load("/home/mb-pro-kg/best23/data/users_processed.json")

        self.culture = []
        for key, element in culture.items():
            for item in element:
                self.culture.append(item)

        self.sightseeing = []
        for key, element in sightseeing.items():
            for item in element:
                self.sightseeing.append(item)

        self.recreation = []
        for key, element in recreation.items():
            for item in element:
                self.recreation.append(item)

        self.users_emb = []
        for key, element in users.items():
            for item in element:
                self.users_emb.append(item)
        
        self.users = {}
        for element in users["users"]:
            user_id = element["user_id"]
            value = {"description": element["description"], "embedding": element["embedding"], "name": element["name"]}
            self.users[user_id] = value

        cultures_names, cultures_similarity_matrix = self.build_similarity_matrix(
            self.culture
        )
        sightseeing_names, sightseeing_similarity_matrix = self.build_similarity_matrix(
            self.sightseeing
        )
        recreation_names, recreation_similarity_matrix = self.build_similarity_matrix(
            self.recreation
        )
        user_names, user_similarity_matrix = self.build_similarity_matrix(
            self.recreation
        )

        self.culture_neighbours = self.build_knn_recommendations(
            cultures_names, cultures_similarity_matrix
        )
        self.sightseeing_neighbours = self.build_knn_recommendations(
            sightseeing_names, sightseeing_similarity_matrix
        )
        self.recreation_neighbours = self.build_knn_recommendations(
            recreation_names, recreation_similarity_matrix
        )
        self.user_neighbours = self.build_knn_recommendations(
            user_names, user_similarity_matrix
        )

    
    def build_knn_recommendations(self, names: list[str], similaritires: np.ndarray) -> dict:
        knn_config = {
            "n_neighbors": 11 if len(names) > 12 else len(names) - 1,
            "metric": "precomputed",
        }

        knn = KNeighborsClassifier(
            **knn_config
        )

        knn.fit(X=similaritires, y=np.zeros(shape=similaritires.shape[0]))
        _, predicted = knn.kneighbors(similaritires, return_distance=True)

        neighbours = {}
        for idx, name in enumerate(names):
            neighbours[name] = [names[pred_idx] for pred_idx in predicted[idx][1:]]

        return neighbours


    def build_similarity_matrix(self, data: dict, name_key: str = "name") -> np.ndarray:
        names = []
        embeddings = []

        for value in data:
            names.append(f"{value[name_key]}")
            embeddings.append(value["embedding"])

        return names, cosine_distances(np.array(embeddings))


    def recommend_for_user(
        self, user_id: int
    ) -> list[tuple[int, str]]:
        cultures_names, cultures_similarity_matrix = self.build_similarity_matrix(
            self.culture + [{"name": user_id, "embedding": self.users[user_id]["embedding"]}]
        )
        sightseeing_names, sightseeing_similarity_matrix = self.build_similarity_matrix(
            self.sightseeing + [{"name": user_id, "embedding": self.users[user_id]["embedding"]}]
        )
        recreation_names, recreation_similarity_matrix = self.build_similarity_matrix(
            self.recreation + [{"name": user_id, "embedding": self.users[user_id]["embedding"]}]
        )

        culture_neighbours = self.build_knn_recommendations(
            cultures_names, cultures_similarity_matrix
        )
        sightseeing_neighbours = self.build_knn_recommendations(
            sightseeing_names, sightseeing_similarity_matrix
        )
        recreation_neighbours = self.build_knn_recommendations(
            recreation_names, recreation_similarity_matrix
        )
        
        return {"culture": culture_neighbours[f"{user_id}"][:3], "sightseeing": sightseeing_neighbours[f"{user_id}"][:3], "recreation": recreation_neighbours[f"{user_id}"][:3]}

    def recommend_search(
        self, text: str
    ) -> list[tuple[int, str]]:
        embedding = EMBEDDER.create_bert_embeddings(
            text
        ).tolist()

        cultures_names, cultures_similarity_matrix = self.build_similarity_matrix(
            self.culture + [{"name": "search", "embedding": embedding}]
        )
        sightseeing_names, sightseeing_similarity_matrix = self.build_similarity_matrix(
            self.sightseeing + [{"name": "search", "embedding": embedding}]
        )
        recreation_names, recreation_similarity_matrix = self.build_similarity_matrix(
            self.recreation + [{"name": "search", "embedding": embedding}]
        )

        culture_neighbours = self.build_knn_recommendations(
            cultures_names, cultures_similarity_matrix
        )
        sightseeing_neighbours = self.build_knn_recommendations(
            sightseeing_names, sightseeing_similarity_matrix
        )
        recreation_neighbours = self.build_knn_recommendations(
            recreation_names, recreation_similarity_matrix
        )
        
        return {"culture": culture_neighbours[f"search"][:3], "sightseeing": sightseeing_neighbours[f"search"][:3], "recreation": recreation_neighbours[f"search"][:3]}


    def recommend_users(
        self, user_id: int
    ) -> list[tuple[int, str]]:
        user_names, user_similarity_matrix = self.build_similarity_matrix(
            self.users_emb, name_key="user_id"
        )

        user_neighbours = self.build_knn_recommendations(
            user_names, user_similarity_matrix
        )

        similar_users = user_neighbours[f"{user_id}"][:3]
        descriptions = [
            self.users[idx]["description"] for idx in similar_users
        ]
        names = [
            self.users[idx]["name"] for idx in similar_users
        ]
        return {"similar_users": similar_users, "descriptions": descriptions, "user_names": names}


model = Recommender()
