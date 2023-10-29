<template>
  <v-col cols="12" md="5" class="py-12">
    Utwórz nowe konto
    <v-form v-model="form" @submit.prevent="onSubmit">
      <v-text-field
        v-model="name"
        :readonly="loading"
        :rules="[required]"
        class="mb-2"
        clearable
        label="Imie"
      ></v-text-field>
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
        placeholder="Wprowadź swoje hasło"
      ></v-text-field>
      <v-textarea
        v-model="description"
        dense
        label="Wprowadź swój Opis"
        :rules="[required]"
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
        Zarejestruj się
      </v-btn>
    </v-form>
  </v-col>
</template>

<script>
export default {
  data: () => ({
    form: false,
    name: null,
    password: null,
    login: null,
    loading: false,
    description: null,
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
          window.location.origin.replace('3000', '8000') + '/register/',
          {
            method: 'POST',
            headers: {
              Accept: 'application/json',
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              password: this.password,
              login: this.login,
              name: this.name,
              description: this.description,
            }),
          }
        )
        if (response.status !== 200) {
          alert(
            'An error occured during registering. Try again with different data'
          )
          this.loading = false
          return
        }
        const data = await response.json()
        if (typeof window !== 'undefined') {
          document.cookie = 'user_id=' + data.user_id
          document.cookie = 'user=' + data.user
        }
        window.location.replace('../../')
      } catch (e) {
        alert('An error occured during registering: ' + e.message)
      }
      this.loading = false
    },
    required(v) {
      return !!v || 'Field is required'
    },
  },
}
</script>
