<template>
  <section id="hero">
    <v-carousel
      height="calc(100vh - 64px)"
      dark
      cycle
      show-arrows-on-hover
      draggable="true"
      hide-delimiter-background
      :interval="interval"
    >
      <v-carousel-item
        v-for="(carousel, carindex) in carouselsData"
        :key="carindex"
        :src="carousel.src"
        class="gradient-fill"
      >
        <v-container fill-height>
          <div style="max-width: 600px">
            <div
              class="text-md-h2 mb-3 text-sm-h3 text-h5 font-weight-black white--text"
            >
              Co mogę Ci znaleźć?
            </div>
            <p class="mb-5 white--text">
              Jestem algorytmem AI specjalizującym się w wyszukiwaniu ciekawych
              miejsc i wydarzeń, bazując na Twoich zainteresowaniach. Napisz mi,
              czego szukasz, a może uda mi się znaleźć coś co Cię zainteresuje
              ;)
            </p>
            <v-btn :x-large="$vuetify.breakpoint.smAndUp" class="my-3 primary"
              >Wyszukaj</v-btn
            >
            <span class="mx-2 my-4"></span>
            <v-text-field
              v-model="query"
              class="mb-2"
              label="Wpisz tutaj zapytanie"
              @click.left="interval = 0"
              @tap="interval = 0"
            ></v-text-field>
          </div>
        </v-container>
      </v-carousel-item>
    </v-carousel>
  </section>
</template>

<script>
export default {
  data() {
    return {
      carouselsData: [
        {
          src: 'pexels-andrea-piacquadio-3884440.jpg',
        },
        {
          src: 'pexels-peter-olexa-4012966.jpg',
        },
        {
          src: 'pexels-thirdman-5961072.jpg',
        },
        {
          src: 'pexels-andrea-piacquadio-3830745.jpg',
        },
      ],
      query: '',
      interval: 10000,
    }
  },
}
</script>

<style>
.gradient-fill .v-responsive__content {
  background: rgb(0, 0, 0);
  background: linear-gradient(
    to right,
    rgba(3, 12, 41, 0.75),
    rgba(5, 11, 31, 0.65)
  );
}
</style>
