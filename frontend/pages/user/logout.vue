<template>
  <div></div>
</template>

<script>
export default {
  mounted() {
    if (typeof window !== 'undefined') {
      document.cookie = 'user_id='
    }
    while (this.getCookie('user_id') !== '') {
      Promise((resolve) => setTimeout(resolve, 1000))
      if (typeof window !== 'undefined') {
        document.cookie = 'user_id='
      }
    }
    window.location.replace('../../')
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
  },
}
</script>
