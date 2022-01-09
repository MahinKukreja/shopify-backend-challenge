<template>
  <div>
    <form required>
      <input v-model="name" type="text" id="name" placeholder="Book Name" />
      <input
        v-model="author"
        type="text"
        id="author"
        placeholder="Book Author"
      />
      <input
        v-model="publisher"
        type="text"
        id="publisher"
        placeholder="Book Publisher"
      />
      <input
        class="submit"
        @click="addBook(name, author, publisher)"
        type="button"
        value="Submit"
      />
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AddForm",
  data() {
    return {
      name: null,
      author: null,
      publisher: null,
    };
  },
  methods: {
    addBook(book_name, book_author, book_publisher) {
      if (
        book_name === null ||
        book_author === null ||
        book_publisher === null
      ) {
        alert("All fields must be filled out");
      } else {
        const new_book = {
          name: book_name,
          author: book_author,
          publisher: book_publisher,
        };
        axios.post("http://127.0.0.1:5000/add_book", new_book).then((res) => {
          alert(res.data.message);
          this.$root.$emit("new-book-added", {
            id: res.data.id,
            name: book_name,
            author: book_author,
            publisher: book_publisher,
          });
        });
      }
    },
  },
};
</script>

<style>
input {
  margin-right: 10px;
  border-radius: 5px;
  padding: 0.5rem;
}

.submit {
  background-color: chartreuse;
}
</style>