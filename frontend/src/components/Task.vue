<template>
  <v-card>
    <v-card-text>
      <div>#{{ filme.id }}</div>
      <p class="ma-0 pa-0 text-h5 text--primary">
        {{ filme.description }}  
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
    filme: {
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
        filme: this.filme.id,
      })
      this.title = ""
    }
  }
}
</script>
