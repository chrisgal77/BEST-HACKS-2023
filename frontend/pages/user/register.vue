<template>
  <v-col cols="12" md="5" class="py-12">
    Utwórz nowe konto
    <v-form v-model="form" @submit.prevent="onSubmit">
      <v-text-field label="Imie"></v-text-field>
      <v-text-field
        v-model="email"
        :readonly="loading"
        :rules="[required]"
        class="mb-2"
        clearable
        label="Email"
      ></v-text-field>
      <v-text-field
        v-model="password"
        :readonly="loading"
        :rules="[required]"
        clearable
        label="Hasło"
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
        Zarejestruj się
      </v-btn>
    </v-form>
  </v-col>
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
          user: this.email,
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

      this.loading = false
    },
    required(v) {
      return !!v || 'Field is required'
    },
  },
}
</script>
