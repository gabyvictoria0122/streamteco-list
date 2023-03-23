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
        @keyup.enter="searchMovies"
      />
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import TasksApi from "@/api/tasks.api.js"


export default {
  name: "SearchMovies",
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  data() {
    return {
      loading: false,
      moviesearch: [],
    }
  },
  mounted() {
    this.getTasks()
  },
  methods: {
    getTasks() {
      this.loading = true
      TasksApi.getTasks().then((data) => {
        this.moviesearch = data.todos
        this.loading = false
      })
    },
  },
}
</script>

<style>

</style>