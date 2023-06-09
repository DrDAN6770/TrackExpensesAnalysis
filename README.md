# TrackExpensesAnalysis
記帳分析

# 動機
解決自己平常記帳時遇到一些小問題，例如:
  * 時間範圍長達一季、半年、一年以上，難以用肉眼判斷
  * 客製化自己想看的結果，趨勢、大幅支出的月份、分析大幅變動的理由等等

# 部分結果
![image](https://github.com/DrDAN6770/TrackExpensesAnalysis/assets/118630187/cc31e70d-aca5-48f3-bfc4-3e48bbf68f74)

![image](https://github.com/DrDAN6770/TrackExpensesAnalysis/assets/118630187/61730d81-199c-483d-a4b9-6fc98690eb10)

![image](https://github.com/DrDAN6770/TrackExpensesAnalysis/assets/118630187/4d2308a0-5b27-4d4b-9b5c-7c95a2cbbfbe)

# data來源
自己平常日常記帳(透過APP)，彙整成csv檔案傳送至目標信箱

# 步驟
1. 導入必要的Python模組，包括imaplib和pandas等。
2. 使用imaplib庫登入到您的電子郵件帳戶，並在需要的情況下進行身份驗證。
3. 使用imaplib庫打開您想要查詢的郵件文件夾（例如"Inbox"）。
4. 使用imaplib庫搜索郵件文件夾，並確定要查詢哪些郵件。
5. 使用imaplib庫檢索郵件的內容，包括主題、發件人、日期等。
6. 使用Python的pandas模組來處理CSV附件，例如將數據加載到數據幀中以進行分析。
7. 在完成所有需要對郵箱進行的操作後，使用imaplib庫關閉與郵箱帳戶的連接。
8. 透過pandas 資料清理資料分析、matplotlib 繪製圖表

