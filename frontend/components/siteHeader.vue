<template>
  <div>
    <v-navigation-drawer v-model="drawer" fixed app temporary>
      <v-list dense>
        <v-list-item-group v-for="(item, i) in items" :key="i" color="primary">
          <v-list-item v-if="!item.submenu" :to="item.to">
            <v-list-item-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title v-text="item.title.toUpperCase()" />
            </v-list-item-content>
          </v-list-item>
          <v-list-group v-else :prepend-icon="item.icon" no-action>
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title
                  v-text="item.title.toUpperCase()"
                ></v-list-item-title>
              </v-list-item-content>
            </template>
            <v-list-item
              v-for="child in item.submenu"
              :key="child.title"
              :to="child.to"
            >
              <v-list-item-content>
                <v-list-item-title v-text="child.title"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar fixed app hide-on-scroll height="64" elevate-on-scroll>
      <v-app-bar-nav-icon class="hidden-md-and-up" @click="drawer = true" />
      <nuxt-link to="/" class="d-flex">
        <Logo />
      </nuxt-link>
      <v-spacer />

      <template v-for="(name, menuitem) in items">
        <template v-if="name.submenu">
          <v-menu
            :key="menuitem"
            open-on-hover
            offset-y
            transition="slide-y-transition"
            bottom
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                plain
                class="py-5 submenubtn hidden-sm-and-down"
                :ripple="false"
                v-bind="attrs"
                style="height: auto"
                v-on="on"
              >
                {{ name.title }}
                <v-icon right small class="mx-0"> mdi-chevron-down </v-icon>
              </v-btn>
            </template>
            <v-list dense>
              <v-list-item
                v-for="(item, index) in name.submenu"
                :key="index"
                link
                :to="item.to"
              >
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </template>
        <v-btn
          v-else
          :key="menuitem"
          depressed
          tile
          plain
          class="py-8 hidden-sm-and-down"
          :to="name.to"
          >{{ name.title }}</v-btn
        > </template
      ><v-spacer />

      <div>{{ username() }}</div>

      <v-btn icon @click="changeThemeColor">
        <v-icon>{{
          $vuetify.theme.dark ? 'mdi-white-balance-sunny' : 'mdi-weather-night'
        }}</v-icon>
      </v-btn>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      clipped: false,
      drawer: false,
      items: [
        {
          icon: 'mdi-folder-home-outline',
          title: 'Strona domowa',
          to: '/',
        },
        {
          icon: 'mdi-account',
          title: 'O nas',
          to: '/about',
        },
        {
          icon: 'mdi-airballoon',
          title: 'Wydarzenia',
          submenu: [
            // {
            //   title: 'Zapisz się',
            //   to: '/events/join',
            // },
            // {
            //   title: 'Wszystkie wydarzenia',
            //   to: '/events/explore',
            // },
            {
              title: 'Wydarzenia dla mnie',
              to: '/events/my',
            },
          ],
        },
        {
          icon: 'mdi-account-multiple',
          title: 'Spotkania',
          submenu: [
            // {
            //   title: 'Zapisz się',
            //   to: '/meetings/join',
            // },
            // {
            //   title: 'Odkrywaj',
            //   to: '/meetings/explore',
            // },
            {
              title: 'Spotkania dla mnie',
              to: '/meetings/my',
            },
          ],
        },
        {
          icon: 'mdi-duck',
          title: 'Cennik',
          to: '/pricing',
        },
        {
          icon: 'mdi-tools',
          title: 'Mój profil',
          to: '/profile',
          submenu: this.userProfileSubpages(),
        },
      ],
    }
  },
  methods: {
    changeThemeColor() {
      if (this.$vuetify.theme.dark === true) {
        this.$vuetify.theme.dark = false
      } else {
        this.$vuetify.theme.dark = true
      }
    },
    userProfileSubpages() {
      if (typeof window !== 'undefined') {
        if (this.getCookie('user_id') === '') {
          return [
            {
              title: 'Zaloguj',
              to: '/user/login',
            },
            {
              title: 'Zarejestruj',
              to: '/user/register',
            },
          ]
        } else {
          return [
            {
              title: 'Zarządzaj profilem',
              to: '/user/manage',
            },
            {
              title: 'Wyloguj',
              to: '/user/logout',
            },
          ]
        }
      }
      return []
    },
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
    username() {
      if (this.getCookie('name') !== '') {
        return 'Hello, ' + this.getCookie('name')
      }
      return ''
    },
  },
}
</script>

<style scoped>
.submenubtn {
  cursor: default;
}
</style>
