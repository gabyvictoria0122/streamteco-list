<template>

  <v-autocomplete
        placeholder="Busque um filme da sua lista"
        prepend-inner-icon="mdi-magnify"
        filled
        dense
        v-model="search"
        :items="moviesearch"
        :loading="userloading"
        :search-input.sync="moviessearch"
        item-text="login"
      />
</template>

<script>
export default {
  name: "SearchMovies",
}
</script>

<style>

</style>