param(
    [string]$BPDir,
    [string]$RPDir
)

$bpManifest = Join-Path $BPDir "manifest.json"
$rpManifest = Join-Path $RPDir "manifest.json"

$bp = Get-Content $bpManifest -Raw | ConvertFrom-Json
$v = $bp.header.version
$newPatch = $v[2] + 1

Write-Host "Version: $($v[0]).$($v[1]).$($v[2]) -> $($v[0]).$($v[1]).$newPatch"

$old = """version"": [$($v[0]), $($v[1]), $($v[2])]"
$new = """version"": [$($v[0]), $($v[1]), $newPatch]"

$oldDesc = "Mighty Vehicles v$($v[0]).$($v[1]).$($v[2])"
$newDesc = "Mighty Vehicles v$($v[0]).$($v[1]).$newPatch"

foreach ($f in @($bpManifest, $rpManifest)) {
    $text = Get-Content $f -Raw
    $text = $text.Replace($old, $new)
    $text = $text.Replace($oldDesc, $newDesc)
    Set-Content $f $text -NoNewline
}
