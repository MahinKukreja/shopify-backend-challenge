<template>
  <div id="app">
    <h1>Add Book</h1>
    <AddForm />
    <h1>Edit Existing Book</h1>
    <EditForm />
    <h1>Current Books</h1>
    <API />
  </div>
</template>

<script>
import API from "./components/API.vue";
import AddForm from "./components/AddForm.vue";
import EditForm from "./components/EditForm.vue";

export default {
  name: "App",
  components: {
    API,
    EditForm,
    AddForm,
  },
};
</script>

<style>
#app {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
