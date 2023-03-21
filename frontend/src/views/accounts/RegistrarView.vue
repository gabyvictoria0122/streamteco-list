<template>
  <v-container>
    <v-row align="center" class="mt-10" no-gutters>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-sheet class="pa-2"> <h1>Cadastro</h1> </v-sheet>
        <v-form>

          <v-text-field
            v-model="username"
            label="Username"
            prepend-inner-icon="mdi-home-account"
            variant="outlined"
            required
            @keyup.enter="registrar"></v-text-field>

          <v-text-field
            v-model="email"
            label="E-Mail"
            prepend-inner-icon="mdi-email-fast-outline"
            variant="outlined"
            required
            @keyup.enter="registrar"></v-text-field>

          <v-text-field
            v-model="password"
            type="password"
            label="Senha"
            prepend-inner-icon="mdi-key-outline"
            variant="outlined"
            required
            @keyup.enter="registrar"></v-text-field>


          <v-btn
            block
            size="large"
            rounded="pill"
            color="primary"
            append-icon="mdi-chevron-right"
            @click="registrar">
            Continue
          </v-btn>
          <v-btn
            class="my-2"
            block
            size="large"
            rounded="pill"
            color="primary"
            variant="outlined"
            :to="{ name: 'base-home' }">
            Voltar
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import { mapState } from "pinia"
import AccountsApi from "@/api/accounts.api.js"
import { useAppStore } from "@/stores/appStore"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  setup() {
    const appStore = useAppStore()
    const accountsStore = useAccountsStore()
    return { appStore, accountsStore }
  },
  data: () => {
    return {
      loading: false,
      valid: false,
      email:"",
      username: "",
      password: "",
      error: false,
      visible: false,
    }
  },
  mounted() {
    console.log(this.loggedUser)
    AccountsApi.whoami().then((response) => {
      if (response.authenticated) {
        this.saveLoggedUser(response.user)
        this.appStore.showSnackbar("Usuário já logado", "warning")
        this.showTasks()
      }
    })
  },
  methods: {
    registrar() {
      this.loading = true
      AccountsApi.registrar(this.username, this.email, this.password)
        .then((response) => {
          if (!response) {
            this.appStore.showSnackbar("Usuário ou senha invalida", "danger")
            return
          }
          this.saveLoggedUser(response.user)
          this.showTasks()
        })
    },
    saveLoggedUser(user) {
      this.error = !user
      if (user) {
        this.accountsStore.setLoggedUser(user)
        this.visible = false
        console.log("logged")
      }
    },
    showTasks() {
      this.$router.push({ name: "tasks-list" })
      console.log("--> tasks")
    },
  }
}
</script>
