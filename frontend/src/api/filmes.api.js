import api from "./config.js"
import apiHelpers from "./helpers.js"

export default {
  getFilmes: () => {
    return new Promise((resolve, reject) => {
      api
        .get("/api/filmes/list")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  addNewFilmes: (description) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/filmes/add", apiHelpers.dataToForm({ description }))
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  deleteFilmes: (filmesId) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/filmes/delete", apiHelpers.dataToForm({ filmesId }))
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
}
