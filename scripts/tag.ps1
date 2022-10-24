<# Tag a commit with the semantic version #>

param (
    [Parameter()]
    [string] $Ref = "HEAD"
)

$commitMsg = git log -1 --pretty=%B $Ref
$SHA = git rev-parse --short $Ref

$match = $commitMsg | Select-String "Version bump to ([0-9]+\.[0-9]+\.[0-9]+)"

# Only tag if the commit has a message like "Version bump to v3.6.4"
if ($null -eq $match) {
    Write-Host "Commit ${SHA} with message '${commitMsg}' does not match the required regex, aborted." `
        -ForegroundColor Red
    exit 1
}

$tagName = "v$($match.Matches.Groups[1])"
git tag -a $tagName -m $tagName $Ref

Write-Host "Tagged commit ${SHA} with tag ${tagName}." -ForegroundColor Yellow
