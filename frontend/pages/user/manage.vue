<template>
  <v-col cols="12" md="5" class="py-12">
    Edytuj swoje dane
    <v-form v-model="form" @submit.prevent="onSubmit">
      <v-text-field label="Imie"></v-text-field>
      <v-text-field
        v-model="email"
        :readonly="loading"
        class="mb-2"
        clearable
        label="Email"
      ></v-text-field>
      <v-text-field
        v-model="password"
        :readonly="loading"
        clearable
        label="Hasło"
        placeholder="Wprowadź swoje hasło"
      ></v-text-field>
      <v-textarea
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
    },
  },
}
</script>
