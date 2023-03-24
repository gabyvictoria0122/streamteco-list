<template>
  <v-card>
    <v-card-text  class="d-flex flex-row mb-6">
      <input type="checkbox" @click="last" v-model="check">
      <p class="ml-3 text-h5 text--primary" :class="{'text-decoration-line-through':check}">
        {{ task.description }}
      </p>
      <div class="text-center">
        <v-dialog
          v-model="dialog"
        >
          <template v-slot:activator="{ props }">
            <v-icon v-bind="props"  @click="editTask(task.id)">
            mdi-pencil
            </v-icon>
          </template>

          <v-card>
            <v-card-text>
              <v-responsive
              class="mx-auto"
              max-width="344"
            >
                <v-text-field
                  v-model=" task.description "
                  clearable
                  hide-details="auto"
                  label="Edite o Título"
                ></v-text-field>
            </v-responsive>
            </v-card-text>
            <div class="d-flex justify-center mb-6">
              <v-card-actions>
                <v-btn color="purple accent-1" block @click="dialog = false">Editar</v-btn>
              </v-card-actions>
              <v-card-actions>
                <v-btn color="purple accent-1" block @click="dialog = false">Close</v-btn>
              </v-card-actions>
            </div>
          </v-card>
        </v-dialog>
      </div>
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
  data: () => ({
    check: false, 
    dialog: false,
    }),
  methods: {
    editTask(task){
      console.log("vai id pra editar", task)
    },
    deleteTask() {
      this.$emit("removeTask", {
        task: this.task.id,
      })
      this.title = ""
    }
  }
}
</script>
