% include('tpl/header.tpl', title='新建-todolist')

<p class="text-left">
            <a href="./todo" class="btn btn-primary" type="button">查看待办</a>
            <a href="./done" class="btn btn-default" type="button">查看已完成</a>
        </p>

<h2 class="text-left">添加一个待办事项:</h2>

<form action="/new" method="GET">
    <input type="text" size="100" maxlength="100" name="task">
    <p class="text-left">
        <input type="submit" name="save" value="保存" class="btn btn-primary">
    </p>
</form>

% include('tpl/footer.tpl')