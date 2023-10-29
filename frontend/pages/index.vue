<template>
  <section id="home">
    <v-row no-gutters>
      <v-col cols="12">
        <SectionsHero />
        <!-- <SectionsIntro />
        <SectionsCalloutBlock /> -->
        <!-- <SectionsFeatures />
        <SectionsBrands />
        <SectionsTestimonials /> -->
      </v-col>
    </v-row>
  </section>
</template>

<script>
export default {
  beforeCreate() {
    this.$vuetify.theme.dark = true
  },
}
</script>
