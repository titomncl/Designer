#ExecutionPolicy RemoteSigned

$EXEC_PATH = $PSScriptRoot

$dev_path = 'E:\DEV'
$prod_path = 'G:\.shortcut-targets-by-id\1LKqbnGUt5-Lrfl9lElekEI0vY2DOIoog\VSPA'

if (Test-Path -Path $dev_path){
    $env:SBS_DESIGNER_PYTHON_PATH = $dev_path
    $env:DEV_ENV = $dev_path
    $env:PFE_ENV = 'D:\VSPA'
}
elseif (Test-Path -Path $prod_path){
    $env:SBS_DESIGNER_PYTHON_PATH = "$prod_path\DEV"
    $env:DEV_ENV = "$prod_path\DEV\main"
    $env:PFE_ENV = $prod_path
}

Start-Process -FilePath "C:\Program Files\Allegorithmic\Substance Designer\Substance Designer.exe"
