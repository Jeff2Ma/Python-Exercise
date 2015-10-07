% include('tpl/header.tpl', title='首页-todolist')
        <div class="flash">
            ID 为{{no}}的代办事宜：{{msg}}
        </div>
<p>            <a href="javascript:history.go(-1);" class="btn btn-default" type="button">返回</a>
</p>

% include('tpl/footer.tpl')