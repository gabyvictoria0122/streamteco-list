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
  emits: ["searchMove"],
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
        let pega = data.todos
        for(var title of pega){
          this.moviesearch.push(title.description )
        }
        this.loading = false
      })
    },
    searchMovies() {
      this.$emit("searchMove", {
        title: this.title,
      })
      this.title = ""
    },
  },
}
</script>

<style>

</style>