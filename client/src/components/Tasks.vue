<template>
    <div class="container">
          <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Tasks</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Task</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Severity Rating</th>
              <th scope="col">Start Date</th>
              <th scope="col">End Date</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Draft Digital Compaign</td>
              <td>5</td>
              <td>12/03/2020</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
            <tr>
              <td>User Reserch</td>
              <td>2</td>
              <td>12/03/2020</td>
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
    </div>
</template>
