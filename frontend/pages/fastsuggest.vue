<template>
  <div></div>
</template>

<script>
export default {
  data: () => ({
    form: false,
    email: null,
    password: null,
    loading: false,
  }),
  mounted() {
    // window.location.replace('../../')
  },
  methods: {
    async onSubmit() {
      if (!this.form) return

      this.loading = true

      const response = await fetch('http://127.0.0.1:8000/register/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          login: this.email,
          password: this.password,
        }),
      })
      if (response.status !== 200) {
        alert(
          'An error occured during registering. Try again with different data'
        )
        this.loading = false
        return
      }
      const data = await response.json()
      if (typeof window !== 'undefined') {
        document.cookie = 'token=' + data.token
        document.cookie = 'user=' + data.user
      }
      window.location.replace('../../')
      this.loading = false
    },
    required(v) {
      return !!v || 'Field is required'
    },
  },
}
</script>
