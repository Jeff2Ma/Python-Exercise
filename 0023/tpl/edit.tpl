% include('tpl/header.tpl', title='编辑留言-留言板')


<h2 class="text-left">编辑留言:</h2>

<form action="/edit/{{no}}" method="GET">
    <p class="text-left">
          <label for="">*昵称:</label><br>
        <input type="text" size="40" maxlength="40" name="name" value="{{old[0]}}" required>
    </p>
    <p class="text-left">
          <label for="">*内容:</label><br>
        <textarea type="text" size="400" maxlength="600" name="comment" required>{{old[1]}}</textarea>
</p>
    <p class="text-left">
        <input type="submit" name="save" value="保存" class="btn btn-primary">
    </p>
</form>

<form action="/delete/{{no}}" method="GET" class="text-left">
    <input type="submit" name="delete" value="删除本条留言" class="btn btn-danger">
</form>

% include('tpl/footer.tpl')