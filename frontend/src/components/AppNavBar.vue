<template>
  <v-app-bar>
    <v-app-bar-title>{{ title }}</v-app-bar-title>
      <v-btn icon="mdi-heart" :to="{ name: 'base-home' }"></v-btn>
      <v-btn
        :prepend-icon="theme === 'light' ? 'mdi-weather-sunny' : 'mdi-weather-night'"
        @click.stop="themeClick"></v-btn>

      <v-btn icon="mdi-dots-vertical">
        <v-icon icon="mdi-dots-vertical" />
        <v-menu activator="parent">
          <v-list>
            <v-list-item :to="{ name: 'accounts-logout' }"> Sair </v-list-item>
          </v-list>
        </v-menu>
      </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: false,
      default: "Streamteco List",
    },
    theme: {
      type: String,
      required: true,
      default: "dark",
    },
  },
  emits: ["themeClick"],
  data: () => {
    return {
      userloading: false,
      moviesearch: [],
      }
  },
  methods: {
    getTasks() {
      console.log("hum?")
      this.loading = true
      TasksApi.getTasks().then((data) => {
        this.moviesearch = data.todos
        this.loading = false
      })
    },
    themeClick() {
      this.$emit("themeClick")
    },
  },
  watch: {
      moviessearch () {
        console.log("hum?")
        this.getTasks()
      },
  }
}
</script>
