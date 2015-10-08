% include('tpl/header.tpl', title='首页-留言板')


<h2 class="text-left">添加留言:</h2>

<form action="/new" method="GET">
    <p class="text-left">
          <label for="">*昵称:</label><br>
        <input type="text" size="40" maxlength="40" name="name" required>
    </p>
    <p class="text-left">
          <label for="">*内容:</label><br>
        <textarea type="text" size="400" maxlength="600" name="comment" required></textarea>
</p>
    <p class="text-left">
        <input type="submit" name="save" value="提交" class="btn btn-primary">

    </p>
</form>


   <h2 class="text-left">当前留言:</h2>
    <blockquote>
        <p class="text-left">注：点击时间可以进入留言编辑页面</p>
    </blockquote>
    <table border="1" cellspacing="0">
         <colgroup>
        <col style="width: 10%;">
        <col style="width: 70%;">
             <col style="width: 20%;">
    </colgroup>

        <thead>
        <tr>
            <th>姓名</th>
            <th>留言内容</th>
            <th>留言时间</th>
        </tr>
        </thead>
         <tbody>
            %for row in rows:
                 <tr>
                     <td>{{row[1]}}</td>
                     <td>{{row[2]}}</td>
                     <td><a href="/edit/{{row[0]}}" class="edit-a">{{row[3]}}</a></td>
                 </tr>
            %end
        </tbody>
    </table>

% include('tpl/footer.tpl')