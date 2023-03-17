<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline"> Filmes </v-card-title>
        </v-card>
      </v-col>

      <v-col cols="12">
        <filmes-form :form-label="'Nova Filme'" @new-task="addNewFilme" />
      </v-col>

      <v-col v-for="item in items" :key="item.id" cols="12">
        <task :task="item" @remove-task="deleteTask"  />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import FilmesApi from "@/api/filmes.api.js"
import Task from "@/components/Task.vue"
import FilmesForm from "@/components/FilmesForm.vue"

export default {
  name: "FilmesList",
  components: { Task, FilmesForm },
  setup() {
    const appStore = useAppStore()
    return { appStore }
  },
  data() {
    return {
      loading: false,
      items: [],
    }
  },
  mounted() {
    this.getFilmes()
  },
  methods: {
    getFilmes() {
      this.loading = true
      FilmesApi.getFilmes().then((data) => {
        this.items = data.todos
        this.loading = false
      })
    },
    addNewFilme(filme) {
      this.loading = true
      FilmesApi.addNewFilmes(filme.title).then((filme) => {
        this.appStore.showSnackbar(`Nova tarefa adicionada #${filme.id}`)
        this.getFilmes()
        this.loading = false
        console.log("oi")
      })
    },
    deleteTask(filme) {
      this.loading = true
      FilmesApi.deleteTask(filme.filme).then((t) => {
        console.log(t)
        this.appStore.showSnackbar(`Tarefa deletada #${t.todo_id}`)
        this.getTasks()
        this.loading = false
        console.log("oi")
      })
    },
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
