## 软件和更新
- “Other Software”中，选择“Canonical合作伙伴软件”
- 登陆Livepatch(如未登陆)

## Synaptic(软件商店/apt)
- ubuntu-restricted-extras(播放所有视频和音乐格式)
- libdvd-pkg(DVD库，播放DVD，需命令行配置)
- flashplugin-installer(风险)
- **apt-xapian-index(Synaptic快速搜索)**
- microcode(Intel)
- **dconf-editor**
- libavcodec-extra(Netflix播放所有视频)
- tlp tlprdw(保护电池寿命) 安装后运行：sudo tlp start

## Dconf-editor
- /org/gnome/shell/extension/dash-to-dock/click-action 关闭默认值-选择'minimize'(最小化窗口动作)
- /org/gnome/shell/extension/dash-to-dock/show-apps-at-top 打开(移动Dock上的Application入口)

## firefox扩展(https://extensions.gnome.org)
- dash to dock
- dash to panel
- User Themes
- Arc Menu

## 添加.themes和.icons文件夹内容
从U盘添加相应的主题和图标

## Dock重影问题解决方案
移除 Gnome Shell Ubuntu Dock 包

这将会从你的系统中完全移除 Ubuntu Dock 扩展，但同时也移除了 ubuntu-desktop 元数据包。
```
sudo apt remove gnome-shell-extension-ubuntu-dock
```

以后撤消更改需重新安装：
```
sudo apt install gnome-shell-extension-ubuntu-dock
```
或者重新安装 ubuntu-desktop 元数据包（这将会安装你可能已删除的任何 ubuntu-desktop 依赖项，包括 Ubuntu Dock）
```
sudo apt install ubuntu-desktop
```

## 地区和语言设置
- 选择“智能拼音”，删除其他






## 减小周期使用
- cat /proc/sys/vm/swappiness
- gedit admin:///etc/sysctl.conf 添加vm.swappiness=10，重启

## 磁盘
- 磁盘，驱动器设置，启动
(如果断电，一些数据在内存中，会导致数据丢失，但这种风险小)

## 减小SSD写入
- 检查trim是否开启(默认开启)：systemctl status fstrim  (enabled)
- gedit admin:///etc/fstab，在<pass>列的errors前，添加'noatime,'，最终为"noatime,errors", 如果有/home分区，也应添加

## 防火墙
- Synaptic安装gufw
- Status: 开启，Rules-方向(Both)-Applications(KDE Connect)

## 启动“开启启动程序”
- sudo sed -i 's/NoDisplay=true/NoDisplay=false/g' /etc/xdg/autostart/*.desktop

