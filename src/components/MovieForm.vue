<template>
  <div>
    <!-- Success message -->
    <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
    </div>

    <!-- Error messages -->
    <div v-if="errors.length > 0" class="alert alert-danger">
      <ul>
        <li v-for="(error, index) in errors" :key="index">
          Error in the {{ error.field }} field – {{ error.message }}
        </li>
      </ul>
    </div>

    <h2>Upload Form</h2>

    <form id="movieForm" @submit.prevent="saveMovie">

      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" id="title" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" id="description" class="form-control"></textarea>
      </div>

      <div class="form-group mb-3">
        <label for="poster" class="form-label">Photo Upload</label>
        <input type="file" name="poster" id="poster" class="form-control" />
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const csrf_token     = ref('')
const successMessage = ref('')
const errors         = ref([])

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then(response => response.json())
    .then(data => {
      csrf_token.value = data.csrf_token
    })
    .catch(error => console.log(error))
}

onMounted(() => {
  getCsrfToken()
})

function saveMovie() {
  // Reset feedback
  successMessage.value = ''
  errors.value = []

  let movieForm  = document.getElementById('movieForm')
  let form_data  = new FormData(movieForm)

  fetch('/api/v1/movies', {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
    .then(response => response.json())
    .then(data => {
        if (data.errors) {
            errors.value = data.errors
        } else {
            successMessage.value = data.message
            document.getElementById('movieForm').reset()  // clears the form
        }
      console.log(data)
    })
    .catch(error => console.log(error))
}
</script>