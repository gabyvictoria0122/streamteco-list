// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import FilmesList from "@/views/filmes/FilmesList.vue"

export default [
  {
    path: "/filmes",
    component: DefaultLayout,
    children: [
      {
        path: "list",
        name: "filmes-list",
        component: FilmesList,
      },
    ],
  },
]
