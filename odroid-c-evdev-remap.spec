Name:           odroid-c-evdev-remap
Version:        0.1.0
Release:        1%{?dist}
Summary:        Keyboard remappings for Hardkernel's ODROID-C

Group:          User Interface/X Hardware Support
License:        BSD
URL:            http://odroid.com/dokuwiki/doku.php?id=en:odroid-c1
Source0:        50-odroid-c-evdev-remap.conf

BuildArch:      noarch

Requires:       xorg-x11-drv-evdev-remap

%description
Code remappings for keyboard codes on the ODROID-C

%prep

%build

%install
install -m0644 -p -D %{SOURCE0} %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/50-odroid-c-evdev-remap.conf

%files
%config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/50-odroid-c-evdev-remap.conf

%changelog
* Tue Dec 08 2015 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Initial package
