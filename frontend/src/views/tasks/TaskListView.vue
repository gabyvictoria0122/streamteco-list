<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline"> Tasks </v-card-title>
        </v-card>
        
      </v-col>
      <v-col cols="6">
        <task-form :form-label="'Nova Tarefa'" @new-task="addNewTask" />
      </v-col>
      <v-col cols="6">
        <search-movies/>
      </v-col>

      <v-col v-for="item in items" :key="item.id" cols="12">
        <task :task="item" @remove-task="deleteTask" @last-item="goEnd"/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"
import TasksApi from "@/api/tasks.api.js"
import Task from "@/components/Task.vue"
import TaskForm from "@/components/TaskForm.vue"
import SearchMovies from "@/components/Search.vue"

export default {
  name: "TasksList",
  components: { Task, TaskForm, SearchMovies },
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
    this.getTasks()
  },
  methods: {
    getTasks() {
      this.loading = true
      TasksApi.getTasks().then((data) => {
        this.items = data.todos
        this.loading = false
      })
    },
    addNewTask(task) {
      this.loading = true
      TasksApi.addNewTask(task.title).then((task) => {
        this.appStore.showSnackbar(`Nova tarefa adicionada #${task.id}`)
        this.getTasks()
        this.loading = false
        console.log("oi")
      })
    },
    deleteTask(task) {
      this.loading = true
      TasksApi.deleteTask(task.task).then((t) => {
        console.log(t)
        this.appStore.showSnackbar(`Tarefa deletada #${t.todo_id}`)
        this.getTasks()
        this.loading = false
        console.log("oi")
      })
    },
    goEnd(task) {
      TasksApi.getTasks().then((data) => {
        this.items = data.todos
        this.loading = false
      })
      const ultimo = this.items.splice(task.id, 1)[0];
      this.items.push(ultimo);
    },
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
