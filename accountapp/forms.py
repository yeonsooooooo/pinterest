from django.contrib.auth.forms import UserCreationForm


#상속을 통해서 UserCreationForm에서 사용하는 것과 유사하게 사용
#하지만 그 형태를 똑같이 사용을 하면, 수정칸에서 입력하는 값이 데이터베이스에 저장되는 상황이 발생(문제점)
class AccountUpdateForm(UserCreationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        #여기서 username을 disabled로 만들어 주면서 클릭을 할 수 없게 만들어줌
