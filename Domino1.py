-- options
local scriptName = [=====[Script for Domino 1.64]=====]
local scriptVersion = '1.0.0'
local scriptAuthor = 'User'
local startToast = ''
-- 0 - no check; 1 - check package only, 2 - check package and build
local checkTarget = 0

local targetName = [=====[Domino]=====]
local targetPkg = 'com.higgs.domino'
local targetVersion = [=====[1.64]=====]
local targetBuild = 164

-- functions

-- init
gg.require('101.0', 16139)

if startToast ~= '' then startToast = '\n'..startToast end
gg.toast(scriptName..' v'..scriptVersion..' by '..scriptAuthor..startToast)

if checkTarget ~= 0 then
	local info = gg.getTargetInfo()
	local check = false
	local current = false
	if checkTarget >= 1 then
		check = targetPkg
		current = info.packageName
	end
	if checkTarget >= 2 then
		check = check..' '..targetVersion..' ('..targetBuild..')'
		current = current..' '..info.versionName..' ('..info.versionCode..')'
	end
	if check ~= current then
		gg.alert('This script for "'..targetName..'" ['..check..'].\nYou select "'..info.label..'" ['..current..'].\nNow script exit.')
		os.exit()
	end
end
local revert = nil

-- main code
gg.processResume()
gg.setRanges(gg.REGION_JAVA_HEAP | gg.REGION_C_HEAP | gg.REGION_C_ALLOC | gg.REGION_C_DATA | gg.REGION_C_BSS | gg.REGION_PPSSPP | gg.REGION_ANONYMOUS | gg.REGION_JAVA | gg.REGION_OTHER | gg.REGION_BAD | gg.REGION_CODE_APP | gg.REGION_CODE_SYS)
gg.searchNumber("800000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
gg.processResume()
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)
gg.refineNumber("800000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_XOR)
gg.refineNumber("800000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.searchNumber("1800000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
gg.processResume()
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)
gg.refineNumber("1800000", gg.TYPE_AUTO, false, gg.SIGN_EQUAL, 0, -1, 0)
revert = gg.getResults(100, nil, nil, nil, nil, nil, nil, nil, nil)
gg.editAll("176000000", gg.TYPE_DWORD)
gg.processResume()
gg.processResume()
gg.timeJump("1:0:9")
