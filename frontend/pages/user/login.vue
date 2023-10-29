<template>
  <v-col cols="12" md="5" class="py-12">
    Zaloguj się
    <v-form v-model="form" @submit.prevent="onSubmit">
      <v-text-field
        v-model="login"
        :readonly="loading"
        :rules="[required]"
        class="mb-2"
        clearable
        label="Login"
      ></v-text-field>
      <v-text-field
        v-model="password"
        :readonly="loading"
        :rules="[required]"
        clearable
        label="Hasło"
        type="password"
        placeholder="Wprowadź swoje hasło"
      ></v-text-field>
      <v-btn
        :disabled="!form"
        :loading="loading"
        block
        color="success"
        size="large"
        type="submit"
        variant="elevated"
      >
        Zaloguj się
      </v-btn>
    </v-form>
  </v-col>
</template>

<script>
export default {
  data: () => ({
    form: false,
    login: null,
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

      try {
        const response = await fetch(
          window.location.origin.replace('3000', '8000') + '/login/',
          {
            method: 'POST',
            headers: {
              Accept: 'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              login: this.login,
              password: this.password,
            }),
          }
        )
        if (response.status !== 200) {
          this.localAlert(
            'An error occured during logging. Try again with different data'
          )
          this.loading = false
          return
        }
        const data = await response.json()
        if (typeof window !== 'undefined') {
          document.cookie = 'user_id=' + data.user_id
        }
        window.location.replace('../../')
      } catch (e) {
        this.localAlert('An error occured during logging: ' + e.message)
      }
      this.loading = false
    },
    localAlert(msg) {},
    required(v) {
      return !!v || 'Field is required'
    },
  },
}
</script>
