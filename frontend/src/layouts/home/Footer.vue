<template>
  <v-footer
    id="home-footer"
    color="grey darken-4"
    dark
    min-height="72"
  >
    <v-container>
      <v-row>
        <v-col
          class="text-center text-md-right"
        >
          문의 : gg@gmail.com
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
  export default {
    name: 'HomeFooter',
  }
</script>

<style lang="sass">
  #home-footer a
    text-decoration: none
</style>
