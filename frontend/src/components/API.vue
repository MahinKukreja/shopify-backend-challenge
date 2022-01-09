<template>
  <div>
    <table>
      <tbody>
        <div>
          <tr>
            <strong>
              <td>ID</td>
              <td>Name</td>
              <td>Author</td>
              <td>Publisher</td>
              <td>Options</td>
            </strong>
          </tr>
        </div>
        <div :key="book" v-for="book in books">
          <tr>
            <td>{{ book.id }}</td>
            <td>{{ book.name }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.publisher }}</td>
            <td>
              <button @click="delBook(book.id)">
                <i class="fas fa-trash-alt"></i>
              </button>
            </td>
          </tr>
        </div>
      </tbody>
    </table>
    <br />
    <ToCSV :books="books" />
  </div>
</template>

<script>
// For API Requests
import axios from "axios";
import ToCSV from "./ToCSV.vue";

export default {
  name: "API",
  components: {
    ToCSV,
  },
  data() {
    // Initialize Data
    return {
      books: [],
      new_book: {},
    };
  },
  methods: {
    delBook(id) {
      axios.delete(`http://127.0.0.1:5000/delete_book/${id}`).then((res) => {
        alert(res.data);
      });
      this.books = this.books.filter((book) => book.id != id);
    },
  },
  created() {
    // Fill Data from API request
    let url = `http://127.0.0.1:5000/books`;
    axios.get(url).then((res) => {
      for (let i = 0; i < res.data.length; i++) {
        this.new_book = {
          id: res.data[i].id,
          name: res.data[i].name,
          author: res.data[i].author,
          publisher: res.data[i].publisher,
        };
        this.books.push(this.new_book);
      }
    });
  },
  mounted() {
    this.$root.$on("new-book-added", (book) => {
      this.books = [...this.books, book];
    });
    this.$root.$on("new-book-edited", (new_book) => {
      this.books = this.books.filter((book) => book.id != new_book.id);
      this.books.splice(new_book.id - 1, 0, new_book);
    });
  },
};
</script>

<style>
table {
  margin: auto;
}

td,
tr {
  min-width: 150px;
}
button {
  background-color: rgb(255, 0, 0);
  padding-left: 15px;
  padding-right: 15px;
  padding-bottom: 6px;
  padding-top: 6px;
}

i {
  color: whitesmoke;
}
</style>