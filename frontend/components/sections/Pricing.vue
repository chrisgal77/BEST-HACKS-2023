<template>
  <section :class="$vuetify.theme.dark ? 'black' : 'white'" class="py-16">
    <v-container>
      <v-row>
        <v-col>
          <v-row no-gutters>
            <v-col class="text-center">
              <h2
                class="text-h4 text-md-h3 text-center font-weight-black text-capitalize mb-4"
              >
                Najdostępniejsze plany płatności
              </h2>

              <p class="my-10 title">
                Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed
                diam nonummy nibh euismod tincidunt ut laoreet dolore magna
                aliquam erat volutpat.
              </p>
              <div class="text-center">
                <v-btn-toggle
                  v-model="planDuration"
                  active-class="primary darken-1"
                  borderless
                  mandatory
                  light
                  color="white"
                >
                  <v-btn value="monthly"> Miesięcznie </v-btn>
                  <v-btn value="yearly"> Rocznie </v-btn>
                </v-btn-toggle>
              </div>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
    <v-container fluid>
      <v-row class="mx-auto" style="max-width: 1200px">
        <v-col v-for="(plan, ix) in plans" :key="`plan-${ix}`" cols="12" md="4">
          <v-hover v-slot="{ hover }">
            <v-card
              :elevation="hover ? 24 : plan.elevation"
              :color="plan.color"
              max-width="400"
              :class="hover ? 'zoom' : 'notzoom'"
              class="mx-auto transition-swing"
            >
              <h3
                class="text-h4 text-center font-weight-black white--text pt-5"
                v-text="plan.plan"
              ></h3>
              <v-card-text
                class="text-center subtitle-1 white--text py-2"
                v-text="plan.description"
              ></v-card-text>
              <v-card-subtitle
                class="text-h5 font-weight-black text-center white--text pt-0"
                >{{ planDuration === 'monthly' ? plan.monthly : plan.yearly }}
                <span class="subtitle-1"
                  >na {{ planDuration === 'monthly' ? 'miesiąc' : 'rok' }}</span
                ></v-card-subtitle
              >
              <v-list>
                <v-list-item
                  v-for="(feature, ik) in plan.features"
                  :key="`feature-${ik}`"
                  dense
                >
                  <v-list-item-icon>
                    <v-icon>
                      {{ feature.icon }}
                    </v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title
                      class="text-capitalize"
                      v-text="feature.text"
                    ></v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-btn
                    color="primary"
                    large
                    block
                    rounded
                    class="mx-auto my-3"
                  >
                    Kup teraz
                  </v-btn>
                </v-list-item>
              </v-list>
            </v-card></v-hover
          >
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
export default {
  data() {
    return {
      planDuration: 'monthly',
      plans: [
        {
          plan: 'Podstawowy',
          elevation: 0,
          color: 'primary darken-1',
          description: 'Podstawowy plan dla użytkownika',
          monthly: '0zł',
          yearly: '0zł',
          features: [
            {
              icon: 'mdi-account-multiple',
              text: 'Dostęp do platformy',
            },
            {
              icon: 'mdi-laptop',
              text: 'Reklamy',
            },
          ],
        },
        {
          plan: 'Plus',
          elevation: 16,
          color: 'green darken-2',
          description: 'Dla tych, którzy nie lubią reklam :)',
          monthly: '4.95zł',
          yearly: '49.95zł',
          features: [
            {
              icon: 'mdi-account-multiple',
              text: 'Dostęp do platformy',
            },
            {
              icon: 'mdi-laptop-off',
              text: 'Brak reklam',
            },
          ],
        },
        {
          plan: 'Donor',
          elevation: 0,
          color: 'orange darken-3',
          description: 'Wsparcie platformy i lokalnych inicjatyw',
          monthly: '4.95zł+',
          yearly: '49.95zł+',
          features: [
            {
              icon: 'mdi-account-multiple',
              text: 'Dostęp do platformy',
            },
            {
              icon: 'mdi-laptop',
              text: 'Reklamy',
            },
            {
              icon: 'mdi-star-circle',
              text: 'Odznaka wspierającego',
            },
            {
              icon: 'mdi-medical-bag',
              text: '50% z przychodu na lokalne inicjatywy',
            },
            {
              icon: 'mdi-heart',
              text: 'Nasza dozgonna wdzięczność <3',
            },
          ],
        },
      ],
    }
  },
}
</script>

<style scoped>
.zoom {
  transform: scale(1.025) translate(0, -10px);
  transition: transform 0.2s;
}
.notzoom {
  transition: transform 0.2s;
}
</style>
