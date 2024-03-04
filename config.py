import g4f

access_token = 'YOUR_ACCESS_TOKEN'
group_name = 'YOUR_GROUP_ID'
prompt_1 = 'YOUR_LONG_COMMENT'
prompt_2 = "YOUR_SHORT_COMMENT"


response = "YOUR_BASIC_COMMENT"
"""
Ваш базовый комментарий, если в посте меньше 5-ти слов
(в таком случает будет сложно составить комментарий к посту оновываясь на его содержимом)
или ни один из хостов не ответит (на всякий случай)
"""


providers = [g4f.Provider.GPTalk, g4f.Provider.GeekGpt, g4f.Provider.AiAsk,
             g4f.Provider.Aichat, g4f.Provider.ChatBase, g4f.Provider.ChatForAi, g4f.Provider.ChatgptAi,
             g4f.Provider.ChatgptX, g4f.Provider.FakeGpt, g4f.Provider.FreeGpt,
             g4f.Provider.GptForLove, g4f.Provider.GptGo, g4f.Provider.Hashnode, g4f.Provider.MyShell,
             g4f.Provider.OpenaiChat, g4f.Provider.Theb, g4f.Provider.You, g4f.Provider.Yqcloud]
