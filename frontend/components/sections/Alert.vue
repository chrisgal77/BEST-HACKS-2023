<template>
  <v-card v-if="alertText?.length > 0" variant="error" color="error">
    <v-card-title>Error!</v-card-title>
    <v-card-text>{{ alertText }}</v-card-text>
    <v-btn color="warning" @click="close">Close</v-btn>
  </v-card>
</template>

<script>
export default {
  props: {
    alertText: {
      type: String,
      default: '',
    },
  },
  methods: {
    close() {
      this.alertText = ''
    },
  },
}
</script>
