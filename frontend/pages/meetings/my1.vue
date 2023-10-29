<template>
  <section :class="this.$vuetify.theme.dark ? '' : 'grey lighten-4'">
    <v-row no-gutters> </v-row>
    <SectionsHeroAlt :hero-alt="heroAlt" />
    <div v-if="allPosts().length === 0">
      Na razie nic tu nie ma, ale nie martw się, wkrótce się coś pojawi!
    </div>
    <v-container v-if="allPosts().length !== 0">
      <div
        v-if="topic?.common_topic"
        class="position-absolute d-flex align-center justify-center w-100 h-100"
      >
        <v-card class="mx-auto">
          <v-card-title class="py-5 font-weight-black">{{
            topic.common_topic
          }}</v-card-title>
        </v-card>
      </div>
      <v-row class="mt-5">
        <v-col>
          <v-row> </v-row>
          <v-row><h1>Do dyskusji pasują:</h1></v-row>
          <v-row v-for="user in topic.recommended_users" :key="user">
            <h3><v-icon>mdi-account</v-icon> {{ user }}</h3>
          </v-row>
          <v-row class="mt-10" />
          <v-row><h1>Ciekawe miejsca na dyskusję:</h1></v-row>
          <v-row v-for="post in allPosts()" :key="post">
            <h3>
              <div v-if="post.type === 'culture'">
                <v-icon>mdi-church</v-icon> {{ post.name }}
              </div>
              <div v-if="post.type === 'recreation'">
                <v-icon>mdi-weight</v-icon> {{ post.name }}
              </div>
              <div v-if="post.type === 'sightseeing'">
                <v-icon>mdi-castle</v-icon> {{ post.name }}
              </div>
            </h3>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <div v-if="allPosts().length !== 0">
      <v-btn color="warning" x-large class="mt-10" block>Zacznij rozmowę</v-btn>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      heroAlt: [
        {
          heading: ' Co powiesz na dyskusję o... ',
        },
      ],
      places: {
        culture: [],
        recreation: [],
        sightseeing: [],
      },
      topic: {},
      loading: false,
    }
  },
  created() {
    this.fetchPlaces()
    this.fetchTopic()
  },
  methods: {
    getCookie(cname) {
      if (typeof window === 'undefined') {
        return ''
      }
      const name = cname + '='
      const decodedCookie = decodeURIComponent(document.cookie)
      const ca = decodedCookie.split(';')
      for (let i = 0; i < ca.length; i++) {
        let c = ca[i]
        while (c.charAt(0) === ' ') {
          c = c.substring(1)
        }
        if (c.indexOf(name) === 0) {
          return c.substring(name.length, c.length)
        }
      }
      return ''
    },
    allPosts() {
      const allposts = []
      for (const post of this.places.culture) {
        const postLocal = {
          name: post.name,
          image: 'data:image/png;base64, ' + post.image,
          type: 'culture',
        }
        allposts.push(postLocal)
      }
      for (const post of this.places.recreation) {
        const postLocal = {
          name: post.name,
          image: 'data:image/png;base64, ' + post.image,
          type: 'recreation',
        }
        allposts.push(postLocal)
      }
      for (const post of this.places.sightseeing) {
        const postLocal = {
          name: post.name,
          image: 'data:image/png;base64, ' + post.image,
          type: 'sightseeing',
        }
        allposts.push(postLocal)
      }
      return allposts
    },
    getColor(type) {
      if (type === 'culture') {
        return 'red darken-2'
      }
      if (type === 'recreation') {
        return 'yellow darken-3'
      }
      return 'green darken-5'
    },
    async fetchTopic() {
      this.loading = true

      try {
        const response = await fetch(
          window.location.origin.replace('3000', '8000') + '/propose-topic/',
          {
            method: 'POST',
            headers: {
              Accept: 'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              user_id: this.getCookie('user_id'),
            }),
          }
        )
        if (response.status !== 200) {
          alert(
            'An error occured during data fetch. Try again with different data'
          )
          this.loading = false
          return
        }
        const data = await response.json()
        this.topic = data
      } catch (e) {
        alert('An error occured during data fetch: ' + e.message)
      }
      this.loading = false
      this.$forceUpdate()
    },
    async fetchPlaces() {
      this.loading = true

      try {
        const response = await fetch(
          window.location.origin.replace('3000', '8000') + '/propose-places/',
          {
            method: 'POST',
            headers: {
              Accept: 'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              user_id: this.getCookie('user_id'),
            }),
          }
        )
        if (response.status !== 200) {
          alert(
            'An error occured during data fetch. Try again with different data'
          )
          this.loading = false
          return
        }
        const data = await response.json()
        this.places = data
      } catch (e) {
        alert('An error occured during data fetch: ' + e.message)
      }
      this.loading = false
      this.$forceUpdate()
    },
  },
  head() {
    return {
      title: 'Może Cię zainteresuje',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content:
            'Infographic hypotheses influencer user experience Long madel ture gen-z paradigm shift client partner network product seilans solve management influencer analytics leverage virality. incubator seed round massmarket. buyer agile development growth hacking business-to-consumer ecosystem',
        },
      ],
    }
  },
}
</script>
