% include('tpl/header.tpl', title='编辑-todolist')
<p class="text-left">
            <a href="/todo" class="btn btn-primary" type="button">查看待办</a>
                <a href="/new" class="btn btn-default" type="button">新建待办</a>
            <a href="/done" class="btn btn-default" type="button">查看已完成</a>
        </p>
<h2 class="text-left">编辑待办任务（ID = {{no}}）</h2>

<form action="/edit/{{no}}" method="get">
<input class="input" type="text" name="task" value="{{old[0]}}" size="100" maxlength="100" style="width: 80%">
    <select name="status" style="width: 18%">
        <option>开启</option>
        <option>关闭</option>
    </select>
<br/>
    <p class="text-left">
        <input type="submit" name="save" value="保存" class="btn btn-primary">
    </p>
</form>

% include('tpl/footer.tpl')