<template>
  <v-col cols="12" md="5" class="py-12">
    Edytuj swoje dane
    <v-form v-model="form" @submit.prevent="onSubmit">
      <v-textarea
        v-model="description"
        dense
        label="Wprowadź swój Opis"
        auto-grow
        rows="8"
        row-height="20"
      ></v-textarea>
      <v-btn
        :disabled="!form"
        :loading="loading"
        block
        color="success"
        size="large"
        type="submit"
        variant="elevated"
      >
        Zaktualizuj
      </v-btn>
    </v-form>
  </v-col>
</template>

<script>
export default {
  data: () => ({
    form: false,
    description: null,
    loading: false,
  }),
  mounted() {
    // window.location.replace('../../')
  },
  methods: {
    async onSubmit() {
      if (!this.form) return

      this.loading = true

      try {
        const response = await fetch(
          window.location.origin.replace('3000', '8000') + '/update/',
          {
            method: 'POST',
            headers: {
              Accept: 'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              description: this.description,
              user_id: this.getCookie('user_id'),
            }),
          }
        )
        if (response.status !== 200) {
          alert('An error occured during update. Try again with different data')
          this.loading = false
          return
        }
        window.location.replace('../../')
      } catch (e) {
        alert('An error occured during update: ' + e.message)
      }
      this.loading = false
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
  },
}
</script>
