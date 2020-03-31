<template>
  <div class="container">
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Tasks</h1>
          <hr />
          <br /><br />
          <button type="button" class="btn btn-success btn-sm" v-b-modal.task-modal>
            Add Task
          </button>
          <br /><br />
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Title</th>
                <th scope="col">Severity Rating</th>
                <th scope="col">Start Date</th>
                <th scope="col">End Date</th>
                <th scope="col">Status?</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(task, index) in tasks" :key="index">
                <td>{{ task.title }}</td>
                <td>{{ task.severity }}</td>
                <td>{{ task.start }}</td>
                <td>{{ task.end }}</td>
                <td>
                  <span v-if="task.done">Complete</span>
                  <span v-else-if="task.pending">Pending</span>
                  <span v-else>Overdue</span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-warning btn-sm">Update</button>
                    <button type="button" class="btn btn-danger btn-sm">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <b-modal ref="addTaskModal" id="task-modal" title="Add a new task" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addTaskForm.title"
            required
            placeholder="Enter title"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-severity-group" label="Title:" label-for="form-severity-input">
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addTaskForm.severity"
            required
            placeholder="Enter Severity"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-start-group" label="Title:" label-for="form-start-input">
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addTaskForm.start"
            required
            placeholder="Enter Start"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-end-group" label="Title:" label-for="form-end-input">
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addTaskForm.end"
            required
            placeholder="Enter End"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-done-group">
          <b-form-checkbox-group v-model="addBookForm.done" id="form-checks">
            <b-form-checkbox value="true">Done?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      tasks: [],
    };
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios
        .get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addTask(payload) {
      const path = 'http://localhost:5000/tasks';
      axios.post(path, payload)
        .then(() => {
          this.getTasks();
          this.message = 'Task added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getTasks();
        });
    },
    initForm() {
      this.addTaskForm.title = '';
      this.addTaskForm.severity = '';
      this.addTaskForm.start = '';
      this.addTaskForm.end = '';
      this.addTaskForm.done = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      let done = false;
      if (this.addTaskForm.done[0]) done = true;
      const payload = {
        title: this.addTaskForm.title,
        severity: this.addTaskForm.severity,
        done, // property shorthand
      };
      this.addTask(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
