// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import FilmeListView from "@/views/filmes/FilmeListView.vue"

export default [
  {
    path: "/filmes",
    component: DefaultLayout,
    children: [
      {
        path: "list",
        name: "filmes-list",
        component: FilmeListView,
      },
    ],
  },
]
