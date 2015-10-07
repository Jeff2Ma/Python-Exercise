% include('tpl/header.tpl', title='首页-todolist')
        <p class="text-left">
            <a href="./new" class="btn btn-primary" type="button">新建待办</a>
            <a href="./done" class="btn btn-default" type="button">查看已完成</a>
        </p>
   <h2 class="text-left">待办事宜:</h2>
    <table border="1" cellspacing="0">
         <colgroup>
        <col style="width: 10%;">
        <col style="width: 70%;">
             <col style="width: 20%;">
    </colgroup>

        <thead>
        <tr>
            <th>序号</th>
            <th>详细内容</th>
            <th>操作</th>
        </tr>
        </thead>
        <tbody>
            %for row in rows:
                %id, title = row
                 <tr>
                     %for col in row:
                        <td>{{col}}</td>
                     %end
                    <td><a href="/edit/{{id}}">编辑</a></td>
                 </tr>
            %end
        </tbody>
    </table>

% include('tpl/footer.tpl')