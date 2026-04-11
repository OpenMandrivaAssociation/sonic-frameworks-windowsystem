%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname SonicFrameworksWindowSystem
%define devname %mklibname SonicFrameworksWindowSystem -d
#define git 20240217

Name: sonic-frameworks-windowsystem
Version: 6.25.0
Release: %{?git:0.%{git}.}1
URL:     https://github.com/Sonic-DE/sonic-frameworks-windowsystem
# %if 0%{?git:1}
# Source0: https://invent.kde.org/frameworks/kwindowsystem/-/archive/master/kwindowsystem-master.tar.bz2#/kwindowsystem-%{git}.tar.bz2
# %else
Source0:  %url/archive/%version/%name-%version.tar.gz
# %endif
Summary: Access to the windowing system
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries

BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DBUILD_WITH_QT6:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-xfixes)
BuildRequires: pkgconfig(xfixes)
Requires: %{libname} = %{EVRD}
Requires: sonic-win
Conflicts: kf6-kwindowsystem

%description
Access to the windowing system

%package -n %{libname}
Summary: Access to the windowing system
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts:  %{_lib}KF6WindowSystem

%description -n %{libname}
Access to the windowing system

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Conflicts:  %{_lib}KF6WindowSystem-devel

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Access to the windowing system

%install -a
%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kwindowsystem.*
%dir %{_qtdir}/plugins/kf6
%dir %{_qtdir}/plugins/kf6/kwindowsystem
%{_qtdir}/qml/org/kde/kwindowsystem
%{_qtdir}/plugins/kf6/kwindowsystem/KF6WindowSystemX11Plugin.so

%files -n %{devname}
%{_includedir}/KF6/KWindowSystem
%{_libdir}/cmake/KF6WindowSystem
%{_libdir}/pkgconfig/KF6WindowSystem.pc

%files -n %{libname}
%{_libdir}/libKF6WindowSystem.so*
