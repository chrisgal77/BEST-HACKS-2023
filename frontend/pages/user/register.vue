<template>
  <v-col cols="12" md="5" class="py-12">
    Zarejestruj nowe konto
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
    onSubmit() {
      if (!this.form) return

      this.loading = true

      setTimeout(() => (this.loading = false), 2000)
      if (typeof window !== 'undefined') {
        document.cookie = 'token=ASDF1234'
      }
    },
    required(v) {
      return !!v || 'Field is required'
    },
  },
}
</script>
