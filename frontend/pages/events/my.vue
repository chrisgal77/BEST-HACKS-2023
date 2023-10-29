<template>
  <div>
    <alert :alert-text="alertText" />
    <section :class="this.$vuetify.theme.dark ? '' : 'grey lighten-4'">
      <v-row no-gutters> </v-row>
      <SectionsHeroAlt :hero-alt="heroAlt" />
      <v-container>
        <v-row>
          <v-col>
            <v-row>
              <div v-if="allPosts().length === 0">
                Na razie nic tu nie ma, ale nie martw się, wkrótce się coś
                pojawi!
              </div>
              <v-col
                v-for="post in allPosts()"
                :key="post"
                sm="6"
                md="6"
                lg="4"
                xl="3"
              >
                <v-card
                  max-width="450"
                  class="mx-auto"
                  elevation="1"
                  :color="getColor(post.type)"
                >
                  <v-img
                    class="white--text align-end"
                    height="200px"
                    :src="post.image"
                  >
                  </v-img>
                  <v-card-subtitle class="pb-0"> </v-card-subtitle>
                  <v-card-text
                    class="title font-weight-bold mt-3 pb-0 text--primary"
                    style="line-height: 1.8rem"
                  >
                    {{ post.name }}
                  </v-card-text>
                  <div v-if="post.type === 'culture'" class="mx-2">
                    <v-icon>mdi-church</v-icon>
                    Kultura
                  </div>
                  <div v-if="post.type === 'recreation'" class="mx-2">
                    <v-icon>mdi-weight</v-icon>
                    Rekreacja
                  </div>
                  <div v-if="post.type === 'sightseeing'" class="mx-2">
                    <v-icon>mdi-castle</v-icon>
                    Zwiedzanie
                  </div>
                </v-card>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </section>
  </div>
</template>

<script>
import alert from '../../components/sections/Alert.vue'

export default {
  components: {
    alert,
  },
  data() {
    return {
      heroAlt: [
        {
          heading: ' Coś nam mówi, że to Cię zainteresuje ;) ',
        },
      ],
      posts: {
        culture: [],
        recreation: [],
        sightseeing: [],
      },
      loading: false,
      alertText: null,
    }
  },
  created() {
    this.fetchData()
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
      for (const post of this.posts.culture) {
        const postLocal = {
          name: post.name,
          image: 'data:image/png;base64, ' + post.image,
          type: 'culture',
        }
        allposts.push(postLocal)
      }
      for (const post of this.posts.recreation) {
        const postLocal = {
          name: post.name,
          image: 'data:image/png;base64, ' + post.image,
          type: 'recreation',
        }
        allposts.push(postLocal)
      }
      for (const post of this.posts.sightseeing) {
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
    async fetchData() {
      // if (!this.form) return

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
          this.localAlert(
            'An error occured during data fetch. Try again with different data'
          )
          this.loading = false
          return
        }
        const data = await response.json()
        this.posts = data
      } catch (e) {
        this.localAlert('An error occured during data fetch: ' + e.message)
      }
      this.loading = false
      this.$forceUpdate()
    },
    localAlert(msg) {
      this.alertText = msg
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
