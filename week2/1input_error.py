class UserInputError(Exception):
    def __init__(self, error_info):
        super().__init__(self, error_info)
        self.error_info = error_info

    def __str__(self):
        return self.error_info


user_input = 'a'
try:
    if not user_input.isdigit():
        raise UserInputError('输入错误!')
except UserInputError as e:
    print(e)
finally:
    del user_input  # 清理内存
