
function Get-AbsPath {
    param (
        [Parameter(Mandatory = $true)]
        [string] $Path
    )
    if (Split-Path $Path -IsAbsolute) {
        return $Path
    }
    return "$PSScriptRoot\$Path"
}

<# Assert script conditions #>

# Run in project's virtual environment to use its interpreter
$venvPath = Resolve-Path (Get-AbsPath "..\.venv")
if ($env:VIRTUAL_ENV -ne $venvPath) {
    Write-Host "Script must be run in the project's activated .venv, aborted." -ForegroundColor Red
    exit 1
}

<# Reminder and confirmation #>

Write-Host "About to build project source. Did you remember to version bump? (y/N) " -NoNewline -ForegroundColor Yellow
$confirmation = Read-Host
if ($confirmation -ne "y") {
    Write-Host "Aborted." -ForegroundColor Red
    exit 1
}

<# Build the whl file #>

$distDir = Get-AbsPath "..\dist"
$buildDir = Get-AbsPath "..\build"  # will be auto-deleted afterwards

python setup.py bdist_wheel `
    --dist-dir $distDir `
    --bdist-dir $buildDir

if ($?) {
    Write-Host "Build succeeded. Remember to update any relevant documentation." -ForegroundColor Green
}
else {
    Write-Host "Build failed." -ForegroundColor Red
    exit $LASTEXITCODE
}
