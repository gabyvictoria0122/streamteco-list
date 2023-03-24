<template>
  <v-card>
    <v-card-text  class="d-flex flex-row mb-6">
      <input type="checkbox" @click="last" v-model="check">
      <p class="ml-3 text-h5 text--primary" :class="{'text-decoration-line-through':check}">
        {{ task.description }}
      </p>
      <v-icon  @click="deleteTask">
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
  data: () => ({check: false,}),
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
