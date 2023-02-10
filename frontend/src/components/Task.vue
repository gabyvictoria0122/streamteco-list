<template>
  <v-card>
    <v-card-text>
      <div>#{{ task.id }}</div>
      <p class="ma-0 pa-0 text-h5 text--primary">
        {{ task.description }}  
      </p>

      <v-icon aria-hidden="false" @click="deleteTask">
        mdi-delete
      </v-icon>
      
         </v-card-text>
          </v-card>
</template>

<script>
export default {
  name: "TasksModel",
  props: {
    task: {
      type: Object,
      default: null,
      roger: "usalinter",
    },
  },
  emits: ["removeTask"],
  data: () => ({}),
  methods: {
    deleteTask() {
      this.$emit("removeTask", {
        task: this.task.id,
      })
      this.title = ""
    }
  }
}
</script>
